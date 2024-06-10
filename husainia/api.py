import frappe
from frappe import _
from frappe.utils.password import check_password

#login with Mobile Number 

@frappe.whitelist(allow_guest=True)
def login_with_mobile_no(mobile_no, password):
    # Fetch the user by mobile number
    user = frappe.db.get_value('User', {'mobile_no': mobile_no}, 'name')

    if user:
        try:
            token = []
            frappe.set_user('Administrator')
            
            user_doc = frappe.get_doc("User", user)
            
            check_password(user, password)
            
            api_key = frappe.generate_hash(length=15)
            
            ur = user_doc.api_key = api_key
            token.append(ur)
            user_doc.save()
            
            frappe.db.commit()
            
            return token
        except frappe.AuthenticationError:
            frappe.throw(_("Invalid login credentials"))
        finally:
            frappe.set_user(user)
    else:
        frappe.throw(_("Invalid login credentials"))


@frappe.whitelist(allow_guest=True)
def login_with__email(email, password):
    # Authenticate user
    login_manager = frappe.auth.LoginManager()
    login_manager.authenticate(email, password)
    login_manager.post_login()
    
    if login_manager.user != "Guest":    
        try:
            token = []
            # Generate token
            user = frappe.get_doc("User", login_manager.user)
            api_key = frappe.generate_hash(length=15)
            
            ur = user.api_key = api_key
            user.save()
            token.append(ur)
            
            frappe.db.commit()
            
            return token
        finally:
            frappe.set_user(login_manager.user)
    else:
        frappe.throw(_("Invalid login credentials"))