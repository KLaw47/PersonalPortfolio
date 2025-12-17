const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000/api"; //reads the next.js env. it starts with next public, so its exposed to the browser. nullish coalescing operation if left side null/undefined, use right side.

export async function fetchAPI(endpoint) {
  const res = await fetch(`${API_BASE}${endpoint}`);
  if (!res.ok) {
    throw new Error(`Failed: ${res.status}`);
  }
  return res.json();
}