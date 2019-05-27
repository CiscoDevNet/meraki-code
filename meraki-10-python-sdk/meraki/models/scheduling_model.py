# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.monday_model
import meraki.models.tuesday_model
import meraki.models.wednesday_model
import meraki.models.thursday_model
import meraki.models.friday_model
import meraki.models.saturday_model
import meraki.models.sunday_model

class SchedulingModel(object):

    """Implementation of the 'Scheduling' model.

    The schedule for the group policy. Schedules are applied to days of the
    week.

    Attributes:
        enabled (bool): Whether scheduling is enabled (true) or disabled
            (false). Defaults to false. If true, the schedule objects for each
            day of the week (monday - sunday) are parsed.
        monday (MondayModel): The schedule object for Monday.
        tuesday (TuesdayModel): The schedule object for Tuesday.
        wednesday (WednesdayModel): The schedule object for Wednesday.
        thursday (ThursdayModel): The schedule object for Thursday.
        friday (FridayModel): The schedule object for Friday.
        saturday (SaturdayModel): The schedule object for Saturday.
        sunday (SundayModel): The schedule object for Sunday.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled":'enabled',
        "monday":'monday',
        "tuesday":'tuesday',
        "wednesday":'wednesday',
        "thursday":'thursday',
        "friday":'friday',
        "saturday":'saturday',
        "sunday":'sunday'
    }

    def __init__(self,
                 enabled=None,
                 monday=None,
                 tuesday=None,
                 wednesday=None,
                 thursday=None,
                 friday=None,
                 saturday=None,
                 sunday=None,
                 additional_properties = {}):
        """Constructor for the SchedulingModel class"""

        # Initialize members of the class
        self.enabled = enabled
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday

        # Add additional model properties to the instance
        self.additional_properties = additional_properties


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        enabled = dictionary.get('enabled')
        monday = meraki.models.monday_model.MondayModel.from_dictionary(dictionary.get('monday')) if dictionary.get('monday') else None
        tuesday = meraki.models.tuesday_model.TuesdayModel.from_dictionary(dictionary.get('tuesday')) if dictionary.get('tuesday') else None
        wednesday = meraki.models.wednesday_model.WednesdayModel.from_dictionary(dictionary.get('wednesday')) if dictionary.get('wednesday') else None
        thursday = meraki.models.thursday_model.ThursdayModel.from_dictionary(dictionary.get('thursday')) if dictionary.get('thursday') else None
        friday = meraki.models.friday_model.FridayModel.from_dictionary(dictionary.get('friday')) if dictionary.get('friday') else None
        saturday = meraki.models.saturday_model.SaturdayModel.from_dictionary(dictionary.get('saturday')) if dictionary.get('saturday') else None
        sunday = meraki.models.sunday_model.SundayModel.from_dictionary(dictionary.get('sunday')) if dictionary.get('sunday') else None

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(enabled,
                   monday,
                   tuesday,
                   wednesday,
                   thursday,
                   friday,
                   saturday,
                   sunday,
                   dictionary)


