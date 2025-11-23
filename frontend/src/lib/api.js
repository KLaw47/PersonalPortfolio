const API_BASE =
  process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000"; //reads the next.js env. it starts with next public, so its exposed to the browser. nullish coalecing operation if left side null/undefined, use right side.

export async function getSomething() {
  const res = await fetch(`${API_BASE}/api/something/`);
  if (!res.ok) {
    throw new Error("Failed to fetch");
  }
  return res.json();
}