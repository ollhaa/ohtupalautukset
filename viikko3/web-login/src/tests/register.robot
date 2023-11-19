*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
#Test Setup  Create User And Go To Login Page
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kallev
    Set Password  kalle123
    Set Password confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password confirmation  kalle123
    Submit Credentials
    Register Should Fail with message  Username is too short

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  kalle
    Set Password  kalleaaa
    Set Password confirmation  kalleaaa
    Submit Credentials
    Register Should Fail with message  Password is not valid
    
Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle111
    Set Password confirmation  kalle222
    Submit Credentials
    Register Should Fail with message  Passwords did not match

*** Keywords ***
Submit Credentials
    Click Button  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Register Should Succeed
    Welcome Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

