# mz_is_building is an internal tag and shouldn't be present on any output
# feature.
assert_no_matching_feature(
    12, 653, 1582, 'buildings',
    { 'mz_is_building': None })