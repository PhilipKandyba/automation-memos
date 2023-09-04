from core import by
from core.web.entities.browser_element import Locator
from core.web.wrappers import page


@page()
class EditorDialogElement:
    DIALOG_CONTAINER = Locator(by.CSS_SELECTOR, ".dialog-container")
    EDITOR_INPUTER = DIALOG_CONTAINER.extend(".common-editor-inputer")
    EDITOR_SUBMIT_BUTTON = DIALOG_CONTAINER.extend("button.confirm-btn")
