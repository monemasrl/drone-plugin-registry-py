from pydantic import BaseModel, EmailStr


class Registry(BaseModel):
    address: str
    username: str
    password: str


class Repository(BaseModel):
    id: int
    uid: int
    user_id: int
    namespace: str
    name: str
    slug: str
    scm: str
    git_http_url: str
    git_ssh_url: str
    link: str
    default_branch: str
    private: bool
    visibility: str
    active: bool
    config: str
    trusted: bool
    protected: bool
    ignore_forks: bool
    ignore_pulls: bool
    cancel_pulls: bool
    timeout: int
    counter: int
    synced: int
    created: int
    updated: int
    version: int


class Build(BaseModel):
    id: int
    repo_id: int
    number: int
    parent: int
    status: str
    error: str
    event: str
    action: str
    link: str
    timestamp: int
    title: str
    message: str
    before: str
    after: str
    ref: str
    source_repo: str
    source: str
    target: str
    author_login: str
    author_name: str
    author_email: str
    author_avatar: str
    sender: str
    cron: str
    deploy_to: str
    deploy_id: int
    started: int
    finished: int
    created: int
    updated: int
    version: int


class RegistryRequest(BaseModel):
    repo: Repository
    build: Build
