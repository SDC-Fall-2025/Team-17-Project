/* Environment loader */
export function getenv (name) {
  switch (name) {
  case 'API_BASE_URL':
    /* Vercel does this for us */
    if (import.meta.env.PROD) {
      return "/api";
    }
    if (import.meta.env.VITE_API_BASE_URL !== undefined) {
      return import.meta.env.VITE_API_BASE_URL;
    }
    console.log(window.location);
    const { protocol, hostname, port } = window.location;
    /* On port 8080, api/bin/httpd does this for us */
    return port === "8080"
      ? `/api` : `${protocol}//${hostname}:8000/api`;
  default:
    return undefined;
  }
}
