from core import by
from core.web.entities.browser_element import BrowserElement
from core.web.wrappers import page


@page()
class DialogElement:
    CONFIRM_BUTTON: BrowserElement = by.CSS_SELECTOR, ".confirm-btn.warning"
