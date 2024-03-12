import pytest

from reecheble_finance.domain.enums.multi_attribute_value_enumeration import MultiAttributeValueEnumBase
from reecheble_finance.domain.enums.multi_attribute_value_enumeration import MultiAttributeEnumValue, InvalidValueIdentity


class TestMultiAttributeEnumerationValue:
    def test_equality(self):
        first_enumeration = MultiAttributeEnumValue(1, "Alias")
        second_enumeration = MultiAttributeEnumValue(1, "Alias", "Description should not really matter")
        third_enumeration = MultiAttributeEnumValue(10, "AnyAlias", "Description")
        fourth_enumeration = MultiAttributeEnumValue(10, "AnyAlias", description=None)
        assert first_enumeration == second_enumeration
        assert third_enumeration == fourth_enumeration

    def test_invalid_value_identity(self):
        with pytest.raises(InvalidValueIdentity):
            MultiAttributeEnumValue("str", "str")

    def test_invalid_alias(self):
        with pytest.raises(InvalidValueIdentity):
            MultiAttributeEnumValue(1, 1)

    def test_non_existing_enumeration(self):
        class Enumeration(MultiAttributeValueEnumBase):
            a = 1, "Alias", "some description"
            b = 2, "SecondAlias"

        enumeration_by_alias = Enumeration.get_by_alias("ThirdAlias")
        enumeration_by_identity = Enumeration.get_by_value_identity(4)
        assert enumeration_by_identity == enumeration_by_alias
        assert enumeration_by_identity is None

    def test_existing_enumeration(self):
        class Enumeration(MultiAttributeValueEnumBase):
            a = 1, "Alias", "some description"
            b = 2, "SecondAlias"

        enumeration_by_alias = Enumeration.get_by_alias("Alias")
        assert enumeration_by_alias == Enumeration.a
