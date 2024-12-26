import os

from selene import browser, be, by, have


def test_form():
    browser.open('/automation-practice-form')

    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")


    browser.element('#firstName').should(be.blank).type('Mike')
    browser.element('#lastName').should(be.blank).type('Voronin')
    browser.element('#userEmail').should(be.blank).type("test@mail.ru")
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('1234567891')


    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').element('[value="8"]').click()
    browser.element('.react-datepicker__year-select').element('[value="1995"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--012').click()


    browser.element('[for=hobbies-checkbox-1]').click()


    browser.element('#uploadPicture').set_value(os.path.abspath('../tests/patriots.png'))


    browser.element('#currentAddress').type('Ленина 1')
    browser.element("#state").click().element(by.text("NCR")).click()
    browser.element("#city").click().element(by.text("Delhi")).click()
