# Autotesting of Europeana web encyclopedia <br>

<picture>
 <source media="(prefers-color-scheme: dark)" srcset="images/europeana_logo_DARKMODE.svg">
 <source media="(prefers-color-scheme: light)" srcset="images/europeana_logo_LIGHTMODE.svg">
 <img alt="Europeana logo" src="images/europeana_logo.svg">
</picture>

<details open>
  <summary> <h3>Contents</h3> [hide/show]</summary>
  <ul>
   <li><a href="#introduction">Introduction</a></li>
   <li><a href="#project-overview">Project Overview</a></li>
   <li><a href="#technologies-and-tools-used">Technologies and Tools Used</a></li>
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
<br>
  Welcome to the Europeana autotesting suite, a project created during my Python automation training at QA.GURU computer science school. The main goal of this project is to demonstrate my current skills in software automated testing and to learn and practice new techniques. The project is built using mainly Python and PyCharm IDE, and new tests will be added as they are developed. While not all site content will be covered by the tests, the suite showcases the necessary skills for software automated testing and quality assurance. This project will continue to grow and evolve over time, so stay tuned for updates! :sunglasses:

 ## Project overview
<br>
This autotesting suite is a practice project created during Python automation training courses at QA.GURU computer science school. The main goal is to showcase and improve the author's test automation skills by implementing tests for the Europeana web encyclopedia. The suite covers the main functionality of the site, including links, login, search, language switching, and others.

The project uses Python, Pytest, and Selenium frameworks for test automation, as well as Allure Reports and Allure TestOps for reporting and test management. Selenoid is used for running tests in a containerized environment. Jenkins is integrated for continuous integration and delivery.

The project is open source and can be accessed on GitHub. Contributions are welcome, and the author plans to continue adding new features and documenting the project to help future automators.

 ## Technologies and Tools Used
<br>
<table align="center"><tr>
<td width= "150" align="center"><a href="https://www.python.org/">
 <img alt="Python" src="https://github.com/Kellerberg/Kellerberg/blob/main/images/python.svg" width="50" height="50"><br><b>Python</b></a></td>
<td width= "150" align="center"><a href="https://docs.pytest.org/">
 <img alt="Pytest" src="https://github.com/Kellerberg/Kellerberg/blob/main/images/pytest.svg" width="50" height="50"><br><b>Pytest</b></a></td>
<td width= "150" align="center"><a href="https://www.selenium.dev/">
 <img alt="Selenium" src="https://github.com/Kellerberg/Kellerberg/blob/main/images/selenium.svg" width="50" height="50"><br><b>Selenium</b></a></td>
<td width= "150" align="center"><a href="https://www.jenkins.io/">
 <img alt="Jenkins" src="https://github.com/Kellerberg/Kellerberg/blob/main/images/jenkins.svg" width="50" height="50"><br><b>Jenkins</b></a></td>
<td width= "150" align="center"><a href="https://aerokube.com/selenoid/">
 <img alt="Selenoid" src="https://github.com/Kellerberg/Kellerberg/blob/main/images/selenoid.svg" width="50" height="50"><br><b>Selenoid</b></a></td>
<td width= "150" align="center"><a href="https://qameta.io/allure-report/">
 <img alt="Allure Report" src="https://github.com/Kellerberg/Kellerberg/blob/main/images/allurereport.svg" width="50" height="50"><br><b>Allure Report</b></a></td>
<td width= "150" align="center"><a href="https://qameta.io/">
 <img alt="Allure TestOps" src="https://github.com/Kellerberg/Kellerberg/blob/main/images/alluretestops.svg" width="50" height="50"><br><b>Allure TestOps</b></a></td>
</tr><table>

## Reporting

<br><b>Why using Allure?</b><br>
Allure Reports is an open-source framework that generates interactive reports with detailed information about test runs. It provides clear test execution results with easy-to-read graphics, logs, and failure details. The reports can be accessed via a web browser or viewed as an HTML file. We utilize Allure Reports in our project to provide a clear and concise summary of the test runs and their results.
