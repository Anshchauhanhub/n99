import dotenv
import os
import sib_api_v3_sdk

dotenv.load_dotenv()

def brevo():
  configuration = sib_api_v3_sdk.Configuration()
  configuration.api_key['api-key'] = os.getenv("BREVO_API_KEY")
  return configuration