import frappe

def address(doc,method='None'):
    
    try:
        for link in doc.links:
            # Check if the link is related to a Customer
            if link.link_doctype == 'Customer':
                customer_doc = frappe.get_doc('Customer', link.link_name)  # Fetch the customer document
                # Only update and save if the address has actually changed
                if customer_doc.customer_primary_address != doc.name:
                    customer_doc.customer_primary_address = doc.name  # Update the primary address
                    customer_doc.save(ignore_permissions=True)  # Save the changes without permission checks

            # Check if the link is related to a Supplier
            elif link.link_doctype == 'Supplier':
                supplier_doc = frappe.get_doc('Supplier', link.link_name)  # Fetch the supplier document
                # Only update and save if the address has actually changed
                if supplier_doc.supplier_primary_address != doc.name:
                    supplier_doc.supplier_primary_address = doc.name  # Update the primary address
                    supplier_doc.save(ignore_permissions=True)  # Save the changes without permission checks

    except frappe.DoesNotExistError:
        frappe.log_error(f"Customer or Supplier not found for doc {doc.name}.")
    except Exception as e:
        frappe.log_error(f"An error occurred while saving Customer or Supplier: {str(e)}")



def update_primary_contact(doc, method=None):
    
    try:
        for link in doc.links:
            if link.link_doctype == 'Supplier':
                supplier_doc = frappe.get_doc('Supplier', link.link_name)  # Fetch the supplier document
                supplier_doc.supplier_primary_contact = doc.name  # Update the primary contact
                supplier_doc.save(ignore_permissions=True)  # Save the changes without permission checks

            elif link.link_doctype == 'Customer':
                customer_doc = frappe.get_doc('Customer', link.link_name)  # Fetch the customer document
                customer_doc.customer_primary_contact = doc.name  # Update the primary contact
                customer_doc.save(ignore_permissions=True)  # Save the changes without permission checks

            else:
                # Handle other link doctype types if needed
                pass

    except frappe.DoesNotExistError:
        frappe.log_error(f"{link.link_doctype} {link.link_name} not found.")
    except Exception as e:
        frappe.log_error(f"An error occurred while saving {link.link_doctype} {link.link_name}: {str(e)}")
