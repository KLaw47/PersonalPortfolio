import { fetchAPI } from '@/lib/api';

export default async function TestPage() {
  const posts = await fetchAPI('/blogposts');
  
  return (
    <div>
      <h1>Blog Posts</h1>
      <pre>{JSON.stringify(posts, null, 2)}</pre>
    </div>
  );
}