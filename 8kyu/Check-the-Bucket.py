def check_the_bucket(bucket):
    if 'gold' in bucket:
        return True
    else:
        return False


check_the_bucket(['stone', 'stone', 'gold', 'stone', 'stone', ])