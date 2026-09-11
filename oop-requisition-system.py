"""
Author: Eunice De Castro (Student ID: 20267230)
Date: September 11, 2026
Course: IT5016 Software Development Fundamentals
Assessment: 3 - Software Research & Practice
"""

class RequisitionSystem:
    """
    LESSON 1: Object Class Structure
    Notes: Groups all properties and logic into a single class.
    """
    requisition_counter = 1
    all_requisitions = []

    def __init__(self, date="", staff_name="", staff_id=""):
        """
        LESSON 2: Initializing object variables
        Notes: Sets up the initial values when creating a new request.
        """
        self.date = date
        self.staff_name = staff_name
        self.staff_id = staff_id
        
        self.req_id = str(10000 + RequisitionSystem.requisition_counter)
        RequisitionSystem.requisition_counter += 1

        self.total = 0.0
        self.status = "Pending"
        self.ref_num = "Not Applicable"

        RequisitionSystem.all_requisitions.append(self)

    def calculate_total(self, items):
        """
        LESSON 3: Calculate total
        Notes: Takes a list of items and sums up prices.
        """
        self.total = 0.0
        for item in items:
            name, price = item[0], item[1]
            self.total += price

    def check_approval(self):
        """
        LESSON 4: Status check
        Notes: Auto-approves under $500 threshold.
        """
        if self.total < 500:
            self.status = "Approved"
            self.ref_num = self.staff_id + self.req_id[-3:]
        else:
            self.status = "Pending"
            self.ref_num = "Not Applicable"

    def update_status(self, new_status):
        """
        LESSON 5: Manual update
        Notes: Lets a manager approve or reject a pending request.
        """
        if new_status.lower() == "approved":
            self.status = "Approved"
            self.ref_num = self.staff_id + self.req_id[-3:]
        else:
            self.status = "Not Approved"
            self.ref_num = "Not Applicable"

    @classmethod
    def print_all(cls):
        """
        LESSON 6: Display all records
        Notes: Loops through all created requests and prints them out.
        """
        print("\n--- ALL REQUISITIONS ---")
        for req in cls.all_requisitions:
            print(f"ID: {req.req_id} | Name: {req.staff_name} | Total: ${req.total:.2f} | Status: {req.status}")

    @classmethod
    def print_stats(cls):
        """
        LESSON 7: Summary statistics
        Notes: Counts approved, pending, and rejected items.
        """
        total_count = len(cls.all_requisitions)
        approved_count = sum(1 for req in cls.all_requisitions if req.status == "Approved")
        pending_count = sum(1 for req in cls.all_requisitions if req.status == "Pending")
        rejected_count = sum(1 for req in cls.all_requisitions if req.status == "Not Approved")

        print("\n--- STATISTICS ---")
        print(f"Total Submitted: {total_count}")
        print(f"Approved: {approved_count}")
        print(f"Pending: {pending_count}")
        print(f"Not Approved: {rejected_count}")


# Main execution test
req1 = RequisitionSystem("28/07/2026", "Eunice De Castro", "DER28")
req1.calculate_total([("Office Desk", 450)])
req1.check_approval()

req2 = RequisitionSystem("04/03/2026", "Elaine De Castro", "RED04")
req2.calculate_total([("Workstation PC", 3500)])
req2.check_approval()
req2.update_status("Not Approved")

req3 = RequisitionSystem("31/05/2026", "Emerald De Castro", "ERD31")
req3.calculate_total([("Dual Monitors", 490)])
req3.check_approval()

# Display reports
RequisitionSystem.print_all()
RequisitionSystem.print_stats()