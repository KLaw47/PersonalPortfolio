import { fetchAPI } from "./api"
const getSingleBlogPost = () => {
    return fetchAPI(`/blogposts/latest/`);
}


export {
    getSingleBlogPost,
}