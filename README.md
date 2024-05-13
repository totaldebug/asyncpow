<a name="readme-top"></a>

[![Release][release-shield]][release-url]
[![Stargazers][stars-shield]][stars-url]
![codecov][codecov-shield]

![GitHub last release date][gh-last-release-date]
![GitHub last commit][gh-last-commit]

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]

[![Lines of code][lines]][lines-url]
![Code size][code-size]

[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/totaldebug/asyncpow">
    <img src=".github/img/logo.png" alt="Logo">
  </a>

  <h3 align="center">AsyncPOW</h3>

  <p align="center">
    Python Overseerr Wrapper, A Python library for interacting with the Overseerr API's
  </p>
    <br />
    <br />
    <a href="https://github.com/totaldebug/asyncpow/issues/new?assignees=&labels=type%2Fbug&template=bug_report.yml">Report Bug</a>
    ·
    <a href="https://github.com/totaldebug/asyncpow/issues/new?assignees=&labels=type%2Ffeature&template=feature_request.yml">Request Feature</a>

</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#compatibility">Compatibility</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#sponsor">Sponsor</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This project is a work in progress, the main branch is being developed on live, which may cause breaking changes until the first full release.

The library returns results in JSON format for ease of use, this also reduces the risk of failue when the APIs are updated.

Type hints and type models are in place where possible (this API has terrible circular dependencies which breaks python), if you notice missing items please create a request to have it fixed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

[![python][python]][python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

* [QuickStart Guide](https://docs.totaldebug.uk/asyncpow/quickstart.html)
* [Full Documentation](https://docs.totaldebug.uk/asyncpow)
* [Release Notes](https://github.com/totaldebug/asyncpow/releases)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Features

* Asynchronous
* Type Checking
* Status - Completed
* Discover - WIP
  * Trending - Completed
* Media - WIP
  * Get - Completed
  * Update Status - Completed
  * Delete
  * Get Watch Data
* User - WIP
  * Get - Completed
  * Bulk Update - Completed
  * Update
  * Delete

## Compatibility

AsyncPOW is built for Python 3.12, and initially the v1 Overseerr API

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

See the [feature requests](https://github.com/totaldebug/asyncpow/labels/type%2Ffeature) for a full list of requested features.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Sponsor

My projects arent possible without the support of the community, please consider donating a small amount to keep these projects alive.

[![Sponsor][Sponsor]][Sponsor-url]

<!-- CONTRIBUTING -->
## Contributing

Got something you would like to add? check out the contributing guide in the [documentation](https://docs.totaldebug.uk/asyncpow/contributing.html)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

[![CC BY-NC-SA 4.0][license-shield]][license-url]

* Copyright © [Total Debug](https://totaldebug.uk).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

* [Discord](https://discord.gg/6fmekudc8Q)
* [Discussions](https://github.com/totaldebug/asyncpow/discussions)
* [Project Link](https://github.com/totaldebug/asyncpow)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Below are a list of resources that I used to assist with this project.

* None at this time

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[release-shield]: https://img.shields.io/github/v/release/totaldebug/asyncpow?color=ff7034&label=Release&sort=semver&style=flat-square
[release-url]: https://github.com/totaldebug/asyncpow/releases
[contributors-shield]: https://img.shields.io/github/contributors/totaldebug/asyncpow.svg?style=flat-square
[contributors-url]: https://github.com/totaldebug/asyncpow/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/totaldebug/asyncpow.svg?style=flat-square
[forks-url]: https://github.com/totaldebug/asyncpow/network/members
[stars-shield]: https://img.shields.io/github/stars/totaldebug/asyncpow.svg?style=flat-square
[stars-url]: https://github.com/totaldebug/asyncpow/stargazers
[issues-shield]: https://img.shields.io/github/issues/totaldebug/asyncpow.svg?style=flat-square
[issues-url]: https://github.com/totaldebug/asyncpow/issues
[license-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-orange.svg?style=flat-square
[license-url]: https://creativecommons.org/licenses/by-nc-sa/4.0/
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/marksie1988
[codecov-shield]: https://img.shields.io/codecov/c/github/totaldebug/asyncpow?style=flat-square

[gh-last-release-date]: https://img.shields.io/github/release-date/totaldebug/asyncpow?style=flat-square&label=Last%20Release%20Date&logo=github&logoColor=white
[gh-last-commit]: https://img.shields.io/github/last-commit/totaldebug/asyncpow.svg?style=flat-square&logo=github&label=Last%20Commit&logoColor=white

[lines]: https://img.shields.io/tokei/lines/github/totaldebug/asyncpow?style=flat-square
[lines-url]: https://github.com/totaldebug/asyncpow
[code-size]: https://img.shields.io/github/languages/code-size/totaldebug/asyncpow?style=flat-square

[Sponsor]: https://img.shields.io/badge/sponsor-000?style=flat-square&logo=githubsponsors&logoColor=red
[Sponsor-url]: https://github.com/sponsors/marksie1988

[python]: https://img.shields.io/badge/Python-blue?style=flat-square&logo=Python&logoColor=white
[python-url]: https://www.python.org/
