# """
# """
# #               1.default except block
# ------------------------------------------------------
# # when
# # we
# # don
# # 't know what kind of error it will occure that time we
# # have
# # to
# # go
# # for default except block
#
# # syntax: --->
# # try:
# #     Error
# #     Line
# # except:
# #     statement
#
# # ex1
# a = 100
# b = 0
# try:
#     print(a / 5)
# except:
#     print("Error Handled")
#
# # ex2
# l = [10, 30, 60, 90]
# try:
#     print(l[13])
# except:
#     print("Error Handled Done")
#
# # ex3
# s = "evening"
# try:
#     print(s.append())
# except:
#     print("error Done")
#
# # ex4
# x = {1: 3, 7: 8, 10: 100}
# try:
#     print(x[8])
# except:
#     print("Key error done")
#
# # ex5
# try:
#     with open("Data.txt") as file:
#         print(http: // file.read())
#         except:
#         print("FileNotFoundError handled")
#
#     """
#
# """
#     2.
#     # specific except block
#     # -----------------------------------------------------------------------
#     # when
#     # we
#     # know
#     # what
#     # kind
#     # of
#     # error
#     # it
#     # will
#     # occure
#     # that
#     # time
#     # we
#     # have
#     # to
#     # go
#     # for specific except block
#
#     # syntax: -->
#     #
#     # try:
#     #     error_line
#     # except Exception_Name:
#     #     statement
#     """
#     a = 100
#     b = 0
#     try:
#         print(a / b)
#     except ZeroDivisionError:
#         print("ZeroDivisionError Handled")
#
#     x = {78: 90, 100: 200}
#     try:
#         print(x[900])
#     except KeyError:
#         print("Key error handled")
#     """
#     """