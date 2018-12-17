# iReporter Endpoints
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention


[![Coverage Status](https://coveralls.io/repos/github/SherylWaga/API2/badge.svg?branch=develop)](https://coveralls.io/github/SherylWaga/API2?branch=develop)
[![Build Status](https://travis-ci.org/SherylWaga/API2.svg?branch=develop)](https://travis-ci.org/SherylWaga/API2)

# Prerequisites
Things you need to run the application;
* Requirements
* virtual environment

` python3 -m venv venv `

` pip install -r requirements.txt `

## Installing
Clone my repository;

` git clone https://github.com/SherylWaga/API.git  `



## Endpoints

You can run the urls on postman
<table >
<th>Method</th>
<th>Url</th>
<th>Description</th>
    <tr>
        <td>POST</td>
        <td>/api/v2/users </td>
        <td>user registration </td>
    </tr>
     <tr>
        <td>POST</td>
         <td>/api/v2/users/login</td>
        <td>User login</td>
    </tr>
    <tr>
        <td>POST</td>
         <td>/api/v2/incidents </td>
        <td>Create an Instance i.e Redflag or Intervention</td>
    </tr>
     <tr>
        <td>GET</td>
         <td>/api/v2/incidents </td>
        <td>View all instances i.e Redflags and Interventions</td>
    </tr>
     <tr>
        <td>GET</td>
         <td>/api/v2/incidents/1 </td>
        <td>View a specific incident i.e Redflag or Intervention</td>
    </tr>
    <tr>
        <td>DELETE</td>
         <td>/api/v2/incidents/1 </td>
        <td>Delete a specific incident i.e Redflag or Intervention</td>
    </tr>
    <tr>
        <td>PUT</td>
         <td>/api/v2/incidents/1 </td>
        <td>Edit  a specific incident i.e Redflag or Intervention location or comment</td>
    </tr>
    <tr>
        <td>PATCH</td>
         <td>/api/v2/incidents/1 </td>
        <td>An admin user can edit a specific incident i.e Redflag or Intervention status</td>
    </tr>
   
</table>
