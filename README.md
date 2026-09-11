# Object-Oriented Requisition Management System

**Author:** Eunice De Castro  
**Student ID:** 20267230  
**Date:** September 11, 2026  
**Course:** IT5016 Software Development Fundamentals  

---

## What this program does
For this project, I converted the requisition system into an Object-Oriented setup. Instead of using separate functions and loose global variables, everything related to a requisition (staff details, costs, approval status) is grouped inside a single `RequisitionSystem` class.

## Key things I learned & practiced
* **Encapsulation:** All the data for a request is stored neatly inside object instances (`self`), keeping the data organized and safe from accidental edits.
* **Class Methods:** I used `@classmethod` functions (`print_all` and `print_stats`) so the class can manage and print summary stats for all created objects at once.
* **Controlled Updates:** Instead of manually changing values anywhere in the code, status changes go through clean methods like `check_approval` and `update_status`.
