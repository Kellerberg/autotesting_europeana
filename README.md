<h2>Autotesting of Europeana web encyclopedia.</h2>

<picture>
 <source media="(prefers-color-scheme: dark)" srcset="images/europeana_logo_DARKMODE.svg">
 <source media="(prefers-color-scheme: light)" srcset="images/europeana_logo_LIGHTMODE.svg">
 <img alt="Europeana logo" src="images/europeana_logo.svg">
</picture>

<details open>
  <summary>Contents [hide/show]</summary>
  <ul>
   <li><a href="#introduction">Introduction</a></li>
   <li><a href="#project-overview">Project Overview</a></li>
   <li><a href="#technologies-and-tools-used">Technologies and Tools Used</a></li>
   <li><a href="#getting-started">Getting Started</a></li>
   <ul>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#running-the-tests">Running the Tests</a></li>
   </ul>
   <li><a href="#test-suites">Test Suites</a></li>
    <ul>
     <li><a href="#smoke-tests">Smoke Tests</a></li>
     <li><a href="#regression-tests">Regression Tests</a></li>
     <li><a href="#performance-tests">Performance Tests</a></li>
    </ul>
    <li><a href="#reporting">Reporting</a></li>
    <ul>
     <li><a href="#allure-reports">Allure Reports</a></li>
     <li><a href="#allure-testops">Allure TestOps</a></li>
    </ul>
    <li><a href="#continuous-integration">Continuous Integration</a></li>
    <ul>
     <li><a href="#jenkins-integration">Jenkins Integration</a></li>
     <li><a href="#github-actions-integration">GitHub Actions Integration</a></li>
    </ul>
    <li><a href="#contributions">Contributions</a></li>
  </p>
</details>

## Introduction

  Welcome to the Europeana autotesting suite, a project created during my Python automation training at QA.GURU computer science school. The main goal of this project is to demonstrate my current skills in software automated testing and to learn and practice new techniques. The project is built using mainly Python and PyCharm IDE, and new tests will be added as they are developed. While not all site content will be covered by the tests, the suite showcases the necessary skills for software automated testing and quality assurance. This project will continue to grow and evolve over time, so stay tuned for updates! :sunglasses:

## Project overview

This autotesting suite is a practice project created during Python automation training courses at QA GURU computer science school. The main goal is to showcase and improve the author's test automation skills by implementing tests for the Europeana web encyclopedia. The suite covers the main functionality of the site, including links, login, search, and language switching.

The project uses Python, pytest, and Selenium frameworks for test automation, as well as Allure Reports and Allure TestOps for reporting and test management. Selenoid is used for running tests in a containerized environment. Jenkins is integrated for continuous integration and delivery.

The project is open source and can be accessed on GitHub. Contributions are welcome, and the author plans to continue adding new features and documenting the project to help future automators.
