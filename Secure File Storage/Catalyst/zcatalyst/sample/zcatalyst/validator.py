""" A module of several validators """

from io import BufferedReader
import re
from .exceptions import CatalystError as ValidationError


def is_valid_email(email):
    """
    validates the given value is a email

    Args:
        email: The value to validate.

    Returns:
        bool: Whether the value is a valid email or not.
    """
    regex = r'^[^@]+@[^@]+$'
    if re.fullmatch(regex, email):
        return True
    return False


def is_bool(value):
    """
    validates the given value is a boolean

    Args:
        value: The value to validate.

    Returns:
        bool: Whether the value is a boolean or not.
    """
    return isinstance(value, bool)


def is_number(value):
    """
    validates the given value is a number

    Args:
        value: The value to validate.

    Returns:
        bool: Whether the value is a number or not.
    """
    return isinstance(value, int)


def is_string(value):
    """
    validates the given value is a string

    Args:
        value: The value to validate.

    Returns:
        bool: Whether the value is a string or not.
    """
    return isinstance(value, str)


def is_list(value):
    """
    validates the given value is a list

    Args:
        value: The value to validate.

    Returns:
        bool: Whether the value is a list or not.
    """
    return isinstance(value, list)


def is_dict(value):
    """
    validates the given value is a dict

    Args:
        value: The value to validate.

    Returns:
        bool: Whether the value is a dict or not.
    """
    return isinstance(value, dict)


def is_set(value):
    """
    validates the given value is a set

    Args:
        value: The value to validate.

    Returns:
        bool: Whether the value is a set or not.
    """
    return isinstance(value, set)


def is_tuple(value):
    """
    validates the given value is a tuple

    Args:
        value: The value to validate.

    Returns:
        bool: Whether the value is a tuple or not.
    """
    return isinstance(value, tuple)


def is_buffered_reader(value):
    """
    validates the given value is a buffered reader or not

    Args:
        value: The value to validate.

    Returns:
        bool: Whether the value is a buffered reader or not.
    """
    return isinstance(value, BufferedReader)


def is_non_empty_string(
        value,
        attr_name: str = None,
        raise_err: bool = None
):
    """
    validates the given value is a non-empty string

    Args:
        value: The value to validate.
        attr_name: The name of the value to use in error.
        raise_err: The Boolean to determine if error needs to be thrown.

    Returns:
        bool: Whether the value is a non-empty string or not.

    Raises:
        ValidationError: If the value is not a non-empty string and raise_err given as True.
    """
    if not is_string(value) or not value:
        if raise_err:
            raise ValidationError(
                'Invalid-Argument',
                f'Value provided for {attr_name} is expected to be a non-empty string.',
                value
            )
        return False
    return True


def is_non_empty_string_or_num(
        value,
        attr_name: str = None,
        raise_err: bool = None
):
    """
    validates the given value is a non-empty string or number

    Args:
        value: The value to validate.
        attr_name: The name of the value to use in error.
        raise_err: The Boolean to determine if error needs to be thrown.

    Returns:
        bool: Whether the value is a valid non-empty string or number.

    Raises:
        ValidationError: If the value is not a non-empty string or number and
            when raise_err given as True.
    """
    if not is_non_empty_string(value) or not is_number(value):
        if raise_err:
            raise ValidationError(
                'Invalid-Argument',
                f'Value provided for {attr_name} is expected to be a non-empty string or number.',
                value
            )
        return False
    return True


def is_non_empty_list(
        value,
        attr_name: str = None,
        raise_err: bool = None
):
    """
    validates the given value is a non-empty list

    Args:
        value: The value to validate.
        attr_name: The name of the value to use in error.
        raise_err: The Boolean to determine if error needs to be thrown.

    Returns:
        bool: Whether the value is a valid non-empty list or not.

    Raises:
        ValidationError: If the value is not a non-empty list and raise_err given as True.
    """
    if not is_list(value) or not value:
        if raise_err:
            raise ValidationError(
                'Invalid-Argument',
                f'Value provided for {attr_name} is expected to be a non-empty list.',
                value
            )
        return False
    return True


def is_non_empty_dict(
        value,
        attr_name: str = None,
        raise_err: bool = None
):
    """
    validates the given value is a non-empty dict

    Args:
        value: The value to validate.
        attr_name: The name of the value to use in error.
        raise_err: The Boolean to determine if error needs to be thrown.

    Returns:
        bool: Whether the value is a valid non-empty dict or not.

    Raises:
        ValidationError: If the value is not a non-empty dict and raise_err given as True.
    """
    if not is_dict(value) or not value:
        if raise_err:
            raise ValidationError(
                'Invalid-Argument',
                f'Value provided for {attr_name} is expected to be a non-empty dict.',
                value
            )
        return False
    return True
