import { redirect, type Handle } from '@sveltejs/kit';
import { pages } from '$lib/content/pages';

// Preserve previously shared links when moving to extensionless routes.
export const handle: Handle = async ({ event, resolve }) => {
  const { pathname, search } = event.url;
  if (pathname.endsWith('.html')) {
    const destination = pathname === '/index.html' ? '/' : pathname.slice(0, -5);
    if (Object.hasOwn(pages, destination)) redirect(308, destination + search);
  }
  return resolve(event);
};
