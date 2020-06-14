"""
This type stub file was generated by pyright.
"""

from . import ansible, docker, local, mech, ssh, vagrant, winrm

EXECUTION_CONNECTORS = { 'docker': docker,'local': local,'ssh': ssh,'winrm': winrm }
ALL_CONNECTORS = { 'ansible': ansible,'docker': docker,'local': local,'mech': mech,'ssh': ssh,'vagrant': vagrant,'winrm': winrm }
