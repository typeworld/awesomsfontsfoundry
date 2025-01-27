# project
import awesomefontsfoundry
from awesomefontsfoundry import definitions


# other
import hotmetal
from flask import request, g

awesomefontsfoundry.app.config["modules"].append("hypertext")

###


class HTML(hotmetal.HotMetal):
    def generate(self):
        return self.GenerateBody()

    def initialize(self):
        self.firstFormElement = False
        self._counter = 0

    def counter(self):
        self._counter += 1
        return self._counter

    def header(self):

        self.JSLink("https://code.jquery.com/jquery-3.4.1.min.js")
        self.CSSLink("/static/css/default.css?v=" + g.instanceVersion)
        self.CSSLink("/static/css/awesomefonts.css?v=" + g.instanceVersion)
        self.CSSLink("https://fonts.googleapis.com/icon?family=Material+Icons+Outlined")
        self.JSLink("/static/js/default.js?v=" + g.instanceVersion)
        self.JSLink("/static/js/awesomefonts.js?v=" + g.instanceVersion)

        self.JSLink("https://unpkg.com/@popperjs/core@2")
        self.JSLink("https://unpkg.com/tippy.js@6")

        self.META(name="viewport", content="width=device-width, initial-scale=1")

        self.META(http_equiv="Content-Security-Policy", content="form-action 'self'")

        # LOGIN
        if "/resetpassword" not in request.path:
            self.DIV(
                id="login",
                class_="widget centered invisible dialog",
                style="width: 500px;",
            )
            self.DIV(class_="dialogContent")

            self.DIV(class_="title loginContent")
            self.P()
            self.T("Log In to Existing Account")
            self._P()
            self._DIV()

            self.DIV(class_="title createAccountContent")
            self.P()
            self.T("Create Type.World Account")
            self._P()
            self._DIV()

            self.DIV(class_="dialogInnerWrapper")
            self.DIV(class_="dialogInnerInnerWrapper")
            self.DIV(class_="dialogInnerInnerInnerWrapper")

            self.FORM()

            self.P(class_="createAccountContent")
            self.LABEL(for_="name")
            self.T("Name")
            self._LABEL()
            self.BR()
            self.BR()
            self.INPUT(id="name", placeholder="John Doe")
            self._P()

            self.P()
            self.LABEL(for_="email")
            self.T("Email")
            self._LABEL()
            self.BR()
            self.BR()
            self.INPUT(id="email", type="email", autocomplete="username", placeholder="johndoe@gmail.com")
            self._P()

            self.P(class_="loginContent")
            self.LABEL(for_="password")
            self.T("Password")
            self._LABEL()
            self.BR()
            self.BR()
            self.INPUT(id="password", type="password", autocomplete="current-password")
            self._P()

            self.P(class_="createAccountContent")
            self.LABEL(for_="newpassword")
            self.T("Repeat Password")
            self._LABEL()
            self.BR()
            self.BR()
            self.INPUT(id="newpassword", type="password", autocomplete="new-password")
            self._P()

            self.P(class_="createAccountContent")
            self.LABEL(for_="newpassword2")
            self.T("Repeat Password")
            self._LABEL()
            self.BR()
            self.BR()
            self.INPUT(id="newpassword2", type="password", autocomplete="new-password")
            self._P()

            self.smallSeparator()
            self.P(class_="loginContent")
            self.T('<a href="/resetpassword">I Forgot My Password ↗</a>')
            self._P()

            self._FORM()

            self._DIV()  # .dialogInnerInnerInnerWrapper
            self._DIV()  # .dialogInnerInnerWrapper

            self.DIV(class_="dialogButtonArea")
            self.DIV(class_="clear")

            self.FORM()

            self.SPAN(class_="loginContent floatleft", style="margin-right: 10px;")

            self.A(
                class_="button",
                onclick="$(this).addClass('disabled'); login($('#username').val(), $('#password').val());",
            )
            self.T("Log In")
            self._A()
            self._SPAN()
            self.SPAN(class_="createAccountContent floatleft", style="margin-right: 10px;")
            self.A(
                class_="button",
                onclick=(
                    "$(this).addClass('disabled'); createUserAccount($('#name').val(), $('#username').val(),"
                    " $('#newpassword').val(), $('#newpassword2').val());"
                ),
            )
            self.T("Create Account")
            self._A()
            self._SPAN()
            self.SPAN(class_="floatleft", style="margin-right: 10px;")
            self.A(class_="button secondary", onclick="hideLogin();")
            self.T("Cancel")
            self._A()
            self._SPAN()

            self._FORM()

            self._DIV()  # .clear
            self._DIV()  # .dialogButtonArea
            self._DIV()  # .dialogInnerWrapper

            self._DIV()  # .dialogContent
            self._DIV()  # login

        self.DIV(id="action")
        self._DIV()

        self.DIV(id="dialog", class_="dialog centered widget")
        self.DIV(class_="dialogContent")
        self._DIV()
        self._DIV()

        self.DIV(id="header")

        self.DIV(class_="clear")
        title = (
            "<p>Welcome to Awesome Fonts, the imaginary independent type foundry that exists to showcase the usage of"
            " the Type.World Sign-In service as well as the Type.World font installation app.</p><p>Please purchase a"
            " few fonts (using a fake credit card number), sign in using the Type.World Sign-In, and see how"
            " the Type.World app loads your fonts.</p>"
        )
        self.DIV(class_="floatleft atom")
        self.A(href="/")
        self.IMG(
            src="/static/images/logo.svg",
            style="width:200px; height: 200px;",
            title=awesomefontsfoundry.tooltip("logo", title),
            alt=title,
        )
        self._A()
        self._DIV()

        self.DIV(class_="floatcenter")
        self.DIV(class_="clear")

        # if g.admin:
        #     self.DIV(class_="floatleft", style="margin-right: 40px;")
        #     self.SPAN(class_="link")
        #     self.A(href="/translations")
        #     self.T("Translation Keywords")
        #     self._A()
        #     self._SPAN()
        #     self.SPAN(class_="link")
        #     self.A(href="/languages")
        #     self.T("Languages")
        #     self._A()
        #     self._SPAN()
        #     self.SPAN(class_="link")
        #     self.A(href="/tracebacks")
        #     self.T("Tracebacks")
        #     self._A()
        #     self._SPAN()
        #     self.SPAN(class_="link")
        #     self.A(href="/admin")
        #     self.T("Admin")
        #     self._A()
        #     self._SPAN()
        #     self._DIV()  # .floatleft

        self.DIV(class_="floatleft")

        self._DIV()  # .floatleft
        self._DIV()  # .clear
        self._DIV()  # .floatcenter

        self.DIV(class_="floatright")
        if g.user:
            self.SPAN(class_="link")
            self.T(g.user.data["userdata"]["scope"]["account"]["data"]["email"])
            self._SPAN()
            self.SPAN(class_="link")
            self.A(href="/account")
            self.T('<span class="material-icons-outlined">account_circle</span> Account')
            self._A()
            self._SPAN()
            self.SPAN(class_="link")
            self.A(onclick="logout();")
            self.T('<span class="material-icons-outlined">logout</span> Log Out')
            self._A()
            self._SPAN()
        else:
            if "/resetpassword" not in request.path:
                self.SPAN(class_="link")
                self.A(
                    onclick=(
                        f"login('{definitions.TYPEWORLD_SIGNIN_URL}',"
                        f" '{awesomefontsfoundry.secret('TYPEWORLD_SIGNIN_CLIENTID')}', window.location.href,"
                        f" '{definitions.TYPEWORLD_SIGNIN_SCOPE}', '{g.session.get('loginCode')}')"
                    )
                )
                self.T('<span class="material-icons-outlined">login</span> Sign In with Type.World')
                self._A()
                self._SPAN()

        # Cart
        products = g.session.get("cart") or []
        title = None
        if products:
            title = awesomefontsfoundry.tooltip("addedtocart", "The fonts have been added to the cart")
        self.SPAN(class_="link", style="margin-top: 15px;")
        self.A(href="/cart", title=title)
        self.T('<span class="material-icons-outlined">shopping_cart</span> Cart')
        self._A()
        if products:
            self.SPAN(class_="cartindicator")
            self.T(len(products))
            self._SPAN()
        self._SPAN()

        self._DIV()

        self._DIV()  # .clear

        self._DIV()  # header

        self.DIV(id="stage")

    def footer(self):

        self._DIV()  # stage

        # self.DIV(id="footer")

        # self.DIV(class_="clear")
        # self.DIV(class_="floatcenter")
        # self.DIV(class_="clear")

        # # About
        # self.SPAN(class_="link floatleft")
        # self.A(href="/about")
        # self.T("About")
        # self._A()
        # self._SPAN()

        # # Map
        # self.SPAN(class_="link floatleft")
        # self.A(href="/map")
        # self.T("Map")
        # self._A()
        # self._SPAN()

        # # Impressum
        # self.SPAN(class_="link floatleft")
        # self.A(href="/impressum")
        # self.T("Impressum")
        # self._A()
        # self._SPAN()

        # # Privacy
        # self.SPAN(class_="link floatleft")
        # self.A(href="/privacy")
        # self.T("Privacy Policy")
        # self._A()
        # self._SPAN()

        # # Cookie Policy
        # self.SPAN(class_="link floatleft")
        # self.A(href="/cookies")
        # self.T("Cookie Policy")
        # self._A()
        # self._SPAN()

        # # Terms
        # self.SPAN(class_="link floatleft")
        # self.A(href="/terms")
        # self.T("Terms & Conditions")
        # self._A()
        # self._SPAN()

        # self._DIV()  # .clear
        # self._DIV()  # .floatcenter
        # self._DIV()  # .clear

        # self._DIV()  # footer

    def separator(self):
        self.DIV(class_="separator")
        self._DIV()

    def smallSeparator(self):
        self.DIV(class_="smallSeparator")
        self._DIV()

    def mediumSeparator(self):
        self.DIV(class_="mediumSeparator")
        self._DIV()

    def label(self, key, label, required=False):

        # 		self.DIV()
        self.LABEL(for_=key)
        self.T(label)
        self._LABEL()
        if required:
            self.SPAN(class_="required")
            self.T("&#x2605;")
            self._SPAN()

    # 		self._DIV()

    def checkBox(self, id_, checked=False):

        self.SPAN(class_="checkbox", style="top: -10px;")
        self.INPUT(
            type="checkbox",
            id=id_,
            checked=checked,
            onchange="deRequiredMissing($(this));",
        )
        self._SPAN()

    def textInput(
        self,
        id_,
        value=None,
        type="text",
        placeholder=None,
        focusForFirstFormElement=True,
    ):

        # self.DIV()
        if type == "textarea":
            self.TEXTAREA(id=id_, name=id_, onkeyup="deRequiredMissing($(this));")
            if value:
                self.T(value)
            self._TEXTAREA()
        else:
            self.INPUT(
                type=type,
                id=id_,
                name=id_,
                value=value,
                onkeyup="deRequiredMissing($(this));",
                placeholder=placeholder,
            )
        # self._DIV()

        if focusForFirstFormElement and not self.firstFormElement:
            self.SCRIPT(type="text/javascript")
            self.T("$('#%s').focus();" % id_)
            self._SCRIPT()
            self.firstFormElement = True

    def area(self, headline=None, class_="scheme1", style=None, id_=None):

        self.DIV(class_="area %s" % class_, style=style, id=id_)
        if headline:
            self.DIV(class_="areaheader")
            self.areaHeadline(headline)
            self._DIV()
        self.DIV(class_="areabody")

    def _area(self):

        self._DIV()
        self._DIV()

    def areaHeadline(self, text):
        self.DIV(class_="headline")
        self.SPAN(class_="headline")
        self.T(text)
        self._SPAN()
        self._DIV()

    def info(self, string):
        self.SCRIPT(type="text/javascript")
        self.T('warning("%s");' % string)
        self._SCRIPT()

    def warning(self, string):
        self.SCRIPT(type="text/javascript")
        self.T('warning("%s");' % string)
        self._SCRIPT()
