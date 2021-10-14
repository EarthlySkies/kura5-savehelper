# Security Policy

In this project, security is a priority. Security vulnerabilities will be
adressed with 48 hours of reporting. Please read this whole document before
making a report. Thank you for using your time to discover a vulnerability 
and reporting it to us.

### Supported Versions

Please note that the project officially supports only the latest releases. 
Due to the static nature of the code and lack of installations, there will
be no backporting of fixes to older versions, even those related to security. 

Make sure you are always running the latest available release.

### Threat model
The project security policy does **NOT** cover the following:
- Vulnerabilities in Python itself
- Vulnerabilities in the underlying operating system
- Vulnerabilities related to Kura5 or the save files
- External file modification before, during or after execution

## Reporting a Vulnerability

If you have found a security vulnerability in the project's code, please do not
open an issue or a pull request as they are public. Instead, please contact the 
head of development directly, in this case the repository owner: [EarthlySkies](https://github.com/EarthlySkies/)

You may encrypt your message with the following PGP key if you wish:

-----BEGIN PGP PUBLIC KEY BLOCK-----

mQGNBGFoWVwBDACZ6ESdg7kmtIAvW9w1ZuaWRbjCdxPg8ptwm+Yjth43EL9YMkdZ
TdnMG0Wz4VKWUZ7YUyCbf9VVGkRC5qznjc1hcqV/e1nfiIkCxemYysOD8rSFQK/8
8bsHFE2lRXTAHT/yBoqG8+XDV4pEwXq7Tg0JAA7wgBmLvmR5fX7s7MjP1rPRNW0v
iX1Q61zQLo4HW6GouZ7aKgRoDH34ryNdAMDVlHGlV/R+6T+VDh6hHg7o6zJ4qR+R
NZU0WjwE3sffQ4KRy7Se8Nw3O7id+UFG2hJFdGYiO8SXQkLGtgp+ZoInvzJmobFn
/iL4tGNU3XU++txxwHRLpXZAIgM46hO6tfpSuB8r9pVGr7batNawrDehEJX50xJw
qEA8HtEdmxFDDhctvFDJlJVKxGZgvSJZrxmo/pvh8gbjq8wuIG6VITJ8FJKk0MhE
26yh1mE9E9jWtWIGSVdc9NbSm42uEVS5C5FipAmCjSTKpoXrHvqLnCsgudHok2/S
ItkKv2QE68QKqIcAEQEAAbQhRWFydGhseVNraWVzIDxlYXJ0aGx5c2tpZXNAcG0u
bWU+iQHOBBMBCAA4FiEEA1JYb4d0t/soqZRdAn6X9y1FOjsFAmFoWVwCGwMFCwkI
BwIGFQoJCAsCBBYCAwECHgECF4AACgkQAn6X9y1FOjt2jwv/RZnUxtj4j2lmgXem
LzEjELk1dGmjZ2jh14wL75os0sPnTMjyiwUZsD1bZs9AgrMiipQIgBSWvhrOvgC6
Ba/ylK58XGyLdE6YJODj8rRwCzPtsChTd6GapwayG5pUQ1H9+d6ViCd2jPaZR/Dw
CcS1twv6yfWaj5xDx1QJGGMDMzeBWTM0I+gu5rGfLlkXAMDqzB6s1l8IH65ZD6Xe
mYxWbt1kqYZhWR818kCbZ3d1likmA7tcH8VHDOxYPkgFFu+cT9yemy/6sEz/DAJf
uiKsK8Wqdets1960O8KlmRTvtBctUW02jOjznsargrKZPuMWAroIJEYLs395VFCa
1fiPxSgmLnhXiMGDQz7NcQ45/WV+6bNlftjhI5+4YZBKRegpLdzCjviNm6qCBYDR
QC9vbH6I9acUwvhT+syLkH153aNjQDCgzqSMmzLCSN0KykAxjgsFYqzyOz6iFjGz
mFo6fv+z5JdZ259EP9BY70GufGCdBb/QiL2KMCaPP+MUB1t/uQGNBGFoWVwBDADu
vpCoSh72/RLrlvsy+Oqj9fWB5rDP1H4HVmkz1bHl6AXn5VDc/e4hJj5LqQD9I3o+
VK4xFxdzIyCFgWs7xg1d3qmAfofqoFU8dBA+wWGZ0xeF9I4zte20gysdOxe2A63F
5cFX1qqYASdPTeWj5jqEvVFxRkhoAf2aKohk7lUiw6ubr+YpFV4poW0dKGVAeCtk
uhWbtVuSHYJExPzedXwdVY0qkZBxG1rzYnykbqnuwcoIFAZNNihtOdyUA5U8l7L4
SavWzvNGdICdtBAYnh2NAAFyoZ9rwAIWPojYFTZyIi7y94YzCaSU8K5IMTN1UtmV
iTNPtYmtwc2ZkbReiGYjvsyT0Rg2HLVHXMmFDXPALpfWoalG8BCUDlM8zCRyqdi2
8e+Klyrhxj44G7UCBvnojE+N7kgPkn/I7ZC6KWX6vZFpSYCw3g9MDI/+9LBFpFi3
U7z3SMgrxN0gZ99GDME9QdIWsIDbpdqWde3HUIkylhpDNSXAJIeJDfpvhUwc7cMA
EQEAAYkBtgQYAQgAIBYhBANSWG+HdLf7KKmUXQJ+l/ctRTo7BQJhaFlcAhsMAAoJ
EAJ+l/ctRTo7zVEL/3st9uMH+jMNzAzyI33YCqSQvF+wbO7DgCDM8vV3xMLikm54
15Qy3nHyAqgPitHKMn22SMfEPaAe+HJznGtDQ+vdpJDCttcC9ZhDZHl6khZY1SOp
B+lJI5wB9+9KkPWKUAaTrI4yolCpcd0Sm/6IcWsoeKn5vVy3XT83taaol9cxL/z3
WrDjLG5frx5ad5I+N/eiLaaOHjflDJz/jLrTJtXJ0AtyHNQO8cSKjMPl0J3lh36d
e5ID9ZSYMaTYzZ4DWqt9ktKOzvPS1aSd/+ffc+2kLOHe0qA8h+HTy83i8cArMAGJ
qaaas7wT1dFKMFTA1cQl87kypG+QOzm37AzZRvpZDPbzcWde8Tdq0Xs3jbeS1kNi
WKj1652H3He0GisgwA1HCUAwibBIq/iBNO8vDiAoFdV86KqFeY7B5awU4D52QXzE
lKIBuotIaGkW24vOtlqWKsmE+X/ZVx9wtT1mwn5Pswx9l9gO9J+GmFxnYHAmP3Uq
5XNOagHFoi68vFyFTg==
=47G7
-----END PGP PUBLIC KEY BLOCK-----
