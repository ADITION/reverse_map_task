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

    # This dictionary counts for each content unit how many views a user made on this content unit. A user is
    # represented by a tuple of 3 user IDs (adition-user-ID, new-user-ID, external-user-ID).
    # Therefore the format is:
    # content-unit-ID -> ( (adition-user-ID, new-user-ID, external-user-ID) -> view-count )
    cu_to_user_ids_count = {
        111111: OrderedDict(
            [((11, 12, '13'), 2)]
        ),
        222222: OrderedDict(
            [((21, 22, '23'), 1),
             ((31, 32, '33'), 1),
             ((41, 42, 'ab'), 1)]
        )
    }

    # This dictionary maps the content unit to its reverse map.
    # A reverse map is a dictionary that maps tag IDs to list of view IDs (these are re-mapped to 1,...,n for each
    # content unit)
    # Note that different views can be made by different users or also by the same user.
    # The format is:
    # content-unit-ID -> (tag-ID -> list of re-mapped view IDs)
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

    reverse_maps = generate_reverse_maps(user_id_to_tag_ids, cu_to_user_ids_count)
    assert reverse_maps == expected_reverse_maps
