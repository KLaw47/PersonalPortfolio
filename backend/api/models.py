from django.conf import settings
from django.db import models


class Tag(models.Model):
    """
    Tags used for both projects and blog posts.
    """

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    """
    A portfolio Project
    """

    # user_id -> Django auth user (the owner of the project)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects",
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    summary = models.TextField(blank=True)  # short card blurb
    description = models.TextField(blank=True)  # long "what I learned" content

    live_url = models.URLField(max_length=255, blank=True)  # deployed project link
    repo_url = models.URLField(max_length=255, blank=True)  # GitHub or other repo

    tags = models.ManyToManyField(
        Tag,
        related_name="projects",
        blank=True,
        help_text="Tags associated with this project.",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title


class BlogPostStatus(models.TextChoices):
    DRAFT = "draft", "Draft"
    PUBLISHED = "published", "Published"


class BlogPost(models.Model):
    """
    Blog posts about what you're working on.
    ERD: `blog_posts` table.
    """

    # author_id -> Django auth user
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blog_posts",
    )

    # project_id can be null – not every post is tied to a project
    project = models.ForeignKey(
        Project,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="blog_posts",
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    excerpt = models.TextField(blank=True)  # short summary for listing pages
    content = models.TextField()  # full post body (Markdown/HTML)

    status = models.CharField(
        max_length=20,
        choices=BlogPostStatus.choices,
        default=BlogPostStatus.DRAFT,
    )

    published_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Set when the post is actually published.",
    )

    tags = models.ManyToManyField(
        Tag,
        related_name="blog_posts",
        blank=True,
        help_text="Tags associated with this blog post.",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def __str__(self) -> str:
        return self.title
