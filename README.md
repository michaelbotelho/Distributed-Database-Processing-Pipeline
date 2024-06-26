<a name="readme-top"></a>
<!--
*** Downloaded and Edited from othneildrew/Best-README-Template. 
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
<!-- [![MIT License][license-shield]][license-url] -->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!--
  <a href="https://github.com/michaelbotelho/Distributed-Database-Processing-Pipeline">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
  -->

  <h2 align="center">Distributed-Database-Processing-Pipeline</h2>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Tech Stack</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

A distributed application designed to efficiently retrieve and process sports events data from various allsportdb.com. Leveraging a distributed architecture, web scraping techniques, and caching mechanisms, the system enables users to query sports events data with ease and reliability.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Tech Stack

#### Tools:
* [![Node][Node.js]][Node-url]
* [![Redis][Redis]][Redis-url]

#### Frameworks:
* [![Flask][Flask.py]][Flask-url]
* [![React][React.js]][React-url]

#### Libraries:
* BeautifulSoup (for web scraping)
* Requests (for making HTTP requests)
* Flask-CORS (for enabling CORS in Flask)
* Redis-Py (Python client for Redis)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




## Getting Started

### Prerequisites

- Node.js  
- Python and Pip
- ```requirements.txt```


### Installation

1. Download and extract the files
2. Create a virtual environment within the project root directory ```python -m venv [venv name]```
3. Activate environment ```[venv name]/Scripts/activate```
4. Install the requirements ```pip install -r requirements.txt```
5. Go to ```Client/myapp``` directory within the project folder
6. Install Node into the directory ```npm install node```
7. Run ```npm install serve``` to enable serving files locally


<p align="right">(<a href="#readme-top">back to top</a>)</p>


 
## Usage

1. In a shell, from within the project root directory, activate the virtual environment ```[venv name]/Scripts/activate```
2. In a shell, from the ```Server/``` directory, run ```python Router.py``` (Run up to 5 servers on one machine)
3. In a separate shell, from the ```Client/myapp``` directory, run ```serve -s build``` every time you want to startup the client
4. Make requests from the Client to the Server and observe both Client and Server output


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [X] Create frontend client interface
- [X] Create backend service to process data
- [X] Create backend service to route and cache data
- [X] Create frontend service to communicate between client and server

See the [open issues](https://github.com/michaelbotelho/Distributed-Database-Processing-Pipeline/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE 
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- CONTACT -->
## Contact

Michael Botelho - [linkedin.com/in/michael-m-botelho][linkedin-url] - michaelmbotelho@outlook.com

Project Link: [https://github.com/michaelbotelho/Distributed-Database-Processing-Pipeline](https://github.com/michaelbotelho/Distributed-Database-Processing-Pipeline)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS 
## Acknowledgments

Resources I found helpful during the development of this project:

* [Img Shields](https://shields.io)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[forks-shield]: https://img.shields.io/github/forks/michaelbotelho/Distributed-Database-Processing-Pipeline.svg?style=for-the-badge
[forks-url]: https://github.com/michaelbotelho/Distributed-Database-Processing-Pipeline/network/members
[stars-shield]: https://img.shields.io/github/stars/michaelbotelho/Distributed-Database-Processing-Pipeline.svg?style=for-the-badge
[stars-url]: https://github.com/michaelbotelho/Distributed-Database-Processing-Pipeline/stargazers
[issues-shield]: https://img.shields.io/github/issues/michaelbotelho/Distributed-Database-Processing-Pipeline.svg?style=for-the-badge
[issues-url]: https://github.com/michaelbotelho/Distributed-Database-Processing-Pipeline/issues
[license-shield]: https://img.shields.io/github/license/michaelbotelho/Distributed-Database-Processing-Pipeline.svg?style=for-the-badge
[license-url]: https://github.com/michaelbotelho/Distributed-Database-Processing-Pipeline/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/michael-m-botelho
[product-screenshot]: images/screenshot.png
[Node.js]: https://img.shields.io/badge/node-6DA55F?style=for-the-badge&logo=node.js&logoColor=white
[Node-url]: https://nodejs.org/en
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Flask.py]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/
[Redis]: https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white
[Redis-url]: https://redis.io/
[gRPC]: https://img.shields.io/badge/grpc-4285F4?style=for-the-badge&logo=google&logoColor=white
[gRPC-url]: https://grpc.io/
