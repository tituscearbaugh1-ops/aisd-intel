// Vercel Edge Middleware — HTTP Basic Auth gate
// Password: aisd2026

export default function middleware(request) {
  const authHeader = request.headers.get('authorization');

  if (authHeader && authHeader.startsWith('Basic ')) {
    try {
      const encoded = authHeader.slice(6); // remove "Basic "
      const decoded = atob(encoded);       // base64 decode
      const password = decoded.split(':').slice(1).join(':'); // everything after first colon

      if (password === 'aisd2026') {
        return; // correct password — let the request through
      }
    } catch (e) {
      // malformed auth header — fall through to 401
    }
  }

  // No auth or wrong password — prompt the browser login dialog
  return new Response('Access denied. Enter the password to continue.', {
    status: 401,
    headers: {
      'WWW-Authenticate': 'Basic realm="AISD Intel — Authorized Access Only"',
      'Content-Type': 'text/plain',
    },
  });
}

export const config = {
  matcher: '/:path*',
};
