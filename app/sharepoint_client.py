from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File
from .config import settings
import io
from typing import List

class SharePointClient:
    def __init__(self):
        self.site_url = f"https://{settings.SHAREPOINT_SITE_HOSTNAME}{settings.SHAREPOINT_SITE_PATH}"
        self.ctx = ClientContext(self.site_url).with_client_credentials(
            settings.CLIENT_ID, settings.CLIENT_SECRET
        )
        # verify connection
        self.ctx.web.get().execute_query()

    def list_docx_templates(self) -> List[str]:
        folder = self.ctx.web.get_folder_by_server_relative_url(
            f"{settings.SHAREPOINT_SITE_PATH}/{settings.DOCUMENT_LIBRARY_PATH}"
        )
        files = folder.files
        self.ctx.load(files)
        self.ctx.execute_query()

        docx_files = [f.properties["Name"] for f in files if f.properties["Name"].lower().endswith(".docx")]
        return docx_files

    def download_file(self, filename: str) -> io.BytesIO:
        server_relative = f"{settings.SHAREPOINT_SITE_PATH}/{settings.DOCUMENT_LIBRARY_PATH}/{filename}"
        resp = File.open_binary(self.ctx, server_relative)
        return io.BytesIO(resp.content)
