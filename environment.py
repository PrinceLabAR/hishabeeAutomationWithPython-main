import allure

def before_all(context):
    allure_dir = "./allure-results"
    context.allure_dir = allure_dir

def after_scenario(context, scenario):
    if scenario.status == "failed":
        context.driver.save_screenshot(f'{context.allure_dir}/screenshot.png')
        with open(f'{context.allure_dir}/screenshot.png', 'rb') as screenshot:
            allure.attach(screenshot.read(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
