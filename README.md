# iReporter Endpoints
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

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
   
</table>