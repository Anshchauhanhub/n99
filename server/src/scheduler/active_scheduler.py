import asyncio
from datetime import datetime
import uuid
from zoneinfo import ZoneInfo

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from src.config.db_config import get_db_connection
from src.model.core.showg_spider import movies_showing

scheduler = AsyncIOScheduler()

async def movies_showing_task(**spider_kwargs):
    """Task function to fetch and store currently showing movies."""
    movies = await movies_showing(**spider_kwargs)

    conn = get_db_connection()

    try:
        with conn.cursor() as cur:
            cur.execute("""
            UPDATE movie_data
            SET movie_titles = %s, updated_at = %s
            WHERE id = SHOWG;
            """, (movies, datetime.now(tz=ZoneInfo('Asia/Kolkata'))))

        conn.commit()
        print("Updated showing movies in showing_movies.")

    except Exception as e:
        print("Connection failed.")
        print(e)

    finally:
        conn.close()


def add_new_job(job_id, date, **spider_kwargs):
    """
    Creates and adds a job to the running scheduler.
    
    :param job_id: Unique string to identify this job
    :param trigger_type: 'interval', 'cron', or 'date'
    :param duration: Duration for the interval trigger
    :param start_date: Start date for the date trigger
    :param spider_kwargs: Keyword arguments to pass to the movies_showing_task
    """
    try:
        # Check if job ID already exists to avoid duplicates
        if scheduler.get_job(job_id):
            print(f"Job {job_id} already exists. Not updating tho.")

        # Add the job to the scheduler
        new_job = scheduler.add_job(
            movies_showing_task,
            'interval',
            id=str(uuid.uuid4()),
            hours=6,
            start_date=date,
            next_run_time=datetime.now(),
            kwargs=spider_kwargs
        )
        print(f"Successfully added Job: {job_id}")
        return new_job
    except Exception as e:
        print(f"Error adding job {job_id}: {e}")



if __name__ == "__main__":

    async def main():
        scheduler.start()
        
        job = add_new_job(
            job_id=str(uuid.uuid4()),
            date=datetime.now(), # Temporarily set to now for testing
            name="inox-janak-place",
            code="SCJN",
            city="national-capital-region-ncr",
            date="20260313"
        )
        
        try:
            while True:
                await asyncio.sleep(1)
        except (KeyboardInterrupt, SystemExit):
            scheduler.shutdown()
            print("Scheduler stopped.")

    asyncio.run(main())