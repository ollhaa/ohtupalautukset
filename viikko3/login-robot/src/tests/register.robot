*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  matti  matti123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  r0vanpera
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  mk  r0vanpera
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle1  r0vanpera
    Output Should Contain  Username is not valid

Register With Valid Username And Too Short Password
    Input Credentials  matti  rr
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  matti  mattiiii
    Output Should Contain  Password is not valid    

*** Keywords ***
Input New Command
    Create User  kalle  kalle123
    Input  new