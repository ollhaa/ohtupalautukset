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

Login After Successful Registration
    Set Username  kallem
    Set Password  kalle124
    Set Password confirmation  kalle124
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  kallem
    Set Password  kalle124
    Submit Credentials Login
    Login Should Succeed

Login After Failed Registration
    Set Username  kallet
    Set Password  kal
    Set Password confirmation  kal
    Submit Credentials
    Register Should Fail with message  Password is too short
    Go To Login Page
    Set Username  kallet
    Set Password  ka
    Submit Credentials Login
    Login Should Fail With Message  Invalid username or password
    

*** Keywords ***
Submit Credentials
    Click Button  Register

Submit Credentials Login
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

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

