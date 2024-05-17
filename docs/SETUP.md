# Setup guide

1. Fork this project, or re-use `main.py`, `requirements.txt` and the `.github` folder
2. Create a [personal access token (classic)](https://github.com/settings/tokens), name it `my-gists` for example, and give it the `gist` scope.
3. Locally, copy `.env.example` file to `.env` and edit the variables
4. In the repository, add this token as a `repository secret` and name it `PERSONAL_ACCESS_TOKEN` (`https://github.com/<USERNAME>/<REPO>/settings/secrets/actions`)
