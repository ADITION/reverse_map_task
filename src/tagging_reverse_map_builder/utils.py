from typing import Optional, List, Dict, Tuple, DefaultDict


def generate_reverse_maps(user_id_to_tag_ids_dict: DefaultDict[str, List[int]],
                          cu_to_user_ids_count: Dict[int, Dict[Tuple[Optional[int], Optional[int],
                                                                     Optional[str]], int]]) \
        -> Dict[int, Dict[int, List[int]]]:
    """Generates a dictionary that maps content unit ID to its reverse map.

    A reverse map here maps the tag ID to the list of view IDs, where all the views were made by users that are tagged
    with this tag ID. Note that several views can be made by the same user.
    For simplicity we map the view IDs to 1,...,n for each content unit, where the 1st view ID found is mapped to
    1, the 2nd to 2, etc.

    Args:
        user_id_to_tag_ids_dict: This dictionary maps a user ID to a list of tag IDs that the user was tagged with.
        cu_to_user_ids_count: This dictionary counts for each content unit how many views a user made on this content
            unit. A user is represented by a tuple of 3 user IDs (adition-user-ID, new-user-ID, external-user-ID).

    Returns:
        cu_to_reverse_map_dict: The dictionary that maps a content unit ID to its reverse map.

    """
    pass
