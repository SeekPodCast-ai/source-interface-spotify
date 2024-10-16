
# Spotify Source Interface

# Project Name

[![Build Status](https://github.com/SeekPodCast-ai/source-interface-spotify/actions/workflows/release.yml/badge.svg)](https://github.com/SeekPodCast-ai/source-interface-spotify/actions)

Spotify Source Interface helps in interacting with Spotify API seamlessly by abstracting the API calls and provides easy to use methods

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Versioning](#versioning)
- [Release Process](#release-process)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

To install this Python package from GitHub:

```bash
pip install git+https://github.com/SeekPodCast-ai/source-interface-spotify.git
```

If you are using **Poetry**, you can add this project as a dependency using:

```bash
poetry add git+https://github.com/SeekPodCast-ai/source-interface-spotify.git
```

---

## Usage

Provide usage examples and explanations here for your Python package. For example:

For information regarding the response structure visit https://developer.spotify.com/documentation/web-api

```python
import os
from source_interface_spotify.interface import SpotifyAPIInterface

# These are mandatory 
os.environ["SPOTIFY_CLIENT_ID"] = '<your spotify API Client ID>'
os.environ["SPOTIFY_CLIENT_SECRET"] = '<your spotify API Client Secret>'

client = SpotifyAPIInterface()
episode = client.get_episode(episode_id='6ZcvVBPQ2ToLXEWVbaw59P')
episodes = client.get_episodes(episode_ids=['6ZcvVBPQ2ToLXEWVbaw59F', '6ZcvVBPQ2ToLXEWVbaw59G'])
show = client.get_show(show_id='6ZcvVBPQ2ToLXEWVbaw59P')
shows = client.get_shows(show_ids=['6ZcvVBPQ2ToLXEWVbaw59F', '6ZcvVBPQ2ToLXEWVbaw59G'])
show_episodes = client.get_show_episodes(show_id='6ZcvVBPQ2ToLXEWVbaw59P')

```

---

## Versioning

This project uses **[Semantic Versioning](https://semver.org/)** and follows these rules:
- **Patch Releases** (`vX.X.1`): Bug fixes.
- **Minor Releases** (`vX.1.X`): New features.
- **Major Releases** (`v1.X.X`): Breaking changes.

We use **[Commitizen](https://commitizen-tools.github.io/commitizen/)** for commit message standardization and automated versioning. Prefixes like `fix:`, `feat:`, and `BREAKING CHANGE:` are used in commit messages to automate version bumps.

---

## Release Process

Releases are automated using **GitHub Actions** and **Commitizen**. Here's how it works:

1. **Commit Formatting**: 
   - We use **commitizen** for enforcing commit messages. 
   - Example commit message formats:
     - `fix: correct login page rendering issue`
     - `feat: add new authentication system`
     - `BREAKING CHANGE: removed deprecated API`

2. **Automated Version Bumps**:
   - Each time a commit with a valid prefix is pushed to the default branch, the version is automatically updated following [Semantic Versioning](https://semver.org/).

3. **GitHub Actions**:
   - CI pipeline is set up using GitHub Actions for builds and tests.
   - Upon merging to `main`, the following actions occur:
     - **Linting** using `pre-commit` (e.g., flake8).
     - **Tests** execution.
     - **Version bump** based on commit messages.
     - A **GitHub release** is automatically created with updated changelog.

4. **Manual Release**:
   If you want to manually create a release, you can do the following:
   - Run `cz bump` locally to bump the version.
   - Push the changes, and a release will be automatically created.

---

## Contributing

To contribute to this project:

1. Clone the repository:
   ```bash
   git clone https://github.com/SeekPodCast-ai/source-interface-spotify.git
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Make your changes following the **commitizen** commit message guidelines.

4. Run pre-commit hooks:
   ```bash
   pre-commit run --all-files
   ```

5. Open a Pull Request.

---

## License

[GPL-3.0 license](https://github.com/SeekPodCast-ai/source-interface-spotify?tab=GPL-3.0-1-ov-file)
