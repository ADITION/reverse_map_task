from collections import OrderedDict, defaultdict

from .utils import generate_reverse_maps


def test_generate_reverse_maps():
    # This dictionary maps all the user IDs (all the 3 user IDs above) to a list of tag IDs that the user was
    # tagged with.
    user_id_to_tag_ids = defaultdict(list, {
        '11': [200],
        '13': [100, 200],
        '21': [100],
        '23': [400],
        '31': [100],
        '32': [100, 300],
        '33': [100],
        '41': [400]
    })

    # This dictionary counts for each banner how many clicks a user made on this banner. A user is
    # represented by a tuple of 3 user IDs (adition-user-ID, new-user-ID, external-user-ID).
    # Therefore the format is:
    # banner-ID -> ( (adition-user-ID, new-user-ID, external-user-ID) -> click-count )
    banner_id_to_user_ids_count = {
        111111: OrderedDict(       # click ids for banner 111111
            [((11, 12, '13'), 2)]  # click ids 1 and 2
        ),
        222222: OrderedDict(       # click ids for banner 222222
            [((21, 22, '23'), 1),  # click id 1
             ((31, 32, '33'), 1),  # click id 2
             ((41, 42, '43'), 1)]  # click id 3
        )
    }

    # This dictionary maps the banner to its reverse map.
    # A reverse map is a dictionary that maps tag IDs to list of click IDs (these are re-mapped to 1,...,n for each
    # banner)
    # Note that different clicks can be made by different users or also by the same user.
    # The format is:
    # banner-ID -> (tag-ID -> list of re-mapped click IDs)
    expected_reverse_maps = {
        111111: {
            100: [1, 2],
            200: [1, 2]
        },
        222222: {
            100: [1, 2],
            300: [2],
            400: [1, 3]
        }
    }

    reverse_maps = generate_reverse_maps(user_id_to_tag_ids, banner_id_to_user_ids_count)
    assert reverse_maps == expected_reverse_maps
