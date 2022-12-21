from rest_framework.throttling import UserRateThrottle

class PruthviThrottle(UserRateThrottle):
    scope = 'Pruthvi'

