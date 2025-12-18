'use client'
import Image from "next/image";
import icon from "../../public/icon.ico"
import { useEffect, useState } from "react";
import { getSingleBlogPost } from "@/lib/blogData";

export default function Home() {
  const [blogpost, setBlogPost] = useState({});

  useEffect(() => {
    getSingleBlogPost().then(setBlogPost)
  }, [])

  useEffect(() => {
    console.warn(blogpost)
  }, [blogpost])

  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-50 font-sans dark:bg-black">
      <main className="flex min-h-screen w-full max-w-3xl flex-col items-center justify-between py-32 px-16 bg-white dark:bg-black sm:items-start">
        <Image
          className="dark:invert"
          src="/icon.ico"
          alt="logo"
          width={100}
          height={20}
          priority
        />
        <div className="flex flex-col items-center gap-6 text-center sm:items-start sm:text-left">
          <h1 className="max-w-xs text-3xl font-semibold leading-10 tracking-tight text-black dark:text-zinc-50">
            Blogpost title
          </h1>
          <p className="max-w-md text-lg leading-8 text-zinc-600 dark:text-zinc-400"> 
           I have some words on this screen, this is where we need the blogpost content
          </p>
        </div>
        <div className="flex flex-col gap-4 text-base font-medium sm:flex-row">
        </div>
      </main>
    </div>
  );
}
