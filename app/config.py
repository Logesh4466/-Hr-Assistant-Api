# app/config.py
from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    # SharePoint
    SHAREPOINT_SITE_HOSTNAME: str = "nihilent.sharepoint.com"
    SHAREPOINT_SITE_PATH: str = "/sites/Demo_Connect"
    DOCUMENT_LIBRARY_PATH: str = "Shared Documents/Hr Documents"

    CLIENT_ID: str
    CLIENT_SECRET: str

    # Azure OpenAI
    AZURE_OPENAI_ENDPOINT: str
    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_DEPLOYMENT_NAME: str
    AZURE_OPENAI_API_VERSION:str

    # Local folder (default provided)
    LOCAL_OUTPUT_FOLDER: str = r"C:\Users\vamsi.gudapati\Desktop\Hr Assisstant\outputs"
 
    # Important for pydantic v2: ignore extra env values
    model_config = ConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
