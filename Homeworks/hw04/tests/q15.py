test = {
  'name': 'Question15',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> isinstance(low_farmers_avg_total_income, int) or isinstance(low_farmers_avg_total_income, float) or isinstance(low_farmers_avg_total_income, np.float64) or isinstance(low_farmers_avg_total_income, np.int64)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import numpy as np
          >>> isinstance(high_farmers_avg_total_income, int) or isinstance(high_farmers_avg_total_income, float) or isinstance(high_farmers_avg_total_income, np.float64) or isinstance(high_farmers_avg_total_income, np.int64)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import numpy as np
          >>> isinstance(avg_prop_farmers, int) or isinstance(avg_prop_farmers, float) or isinstance(avg_prop_farmers, np.float64) or isinstance(avg_prop_farmers, np.int64)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import numpy as np
          >>> isinstance(avg_prop_farmers, int) or isinstance(avg_prop_farmers, float) or isinstance(avg_prop_farmers, np.float64) or isinstance(avg_prop_farmers, np.int64)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> q15_answer == 1 or q15_answer == 2
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
