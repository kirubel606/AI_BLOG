from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

class MediaXFrameMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Remove X-Frame-Options header for PDF files under MEDIA_URL
        media_url = settings.MEDIA_URL
        if request.path.startswith(media_url) and response.get('Content-Type', '').startswith('application/pdf'):
            # Pop the header to allow framing from any origin or add specific domain
            response.headers.pop('X-Frame-Options', None)
        return response
