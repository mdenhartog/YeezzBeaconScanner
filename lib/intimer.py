# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Linter
# pylint: disable=E0401,R0903,R0201,C0103

"""
InnovateNow timer module
"""
import sys
import machine

# Initialize logging
import inlogging as logging
log = logging.getLogger(__name__)

class Timer(object):
    """
    Timer class
    """
    def __init__(self, seconds=0, callback=None):
        """
        Init timer
        """
        self._alarm = machine.Timer.Alarm(handler=callback, s=seconds)

class ResetTimer(Timer):
    """
    Reset the device after the timer expires
    """

    def __init__(self, seconds=0):
        """
        Init reset Timer
        """
        super(ResetTimer, self).__init__(seconds, self._reset_handler)

    def _reset_handler(self, alarm):
        """
        Reset the device
        """
        if alarm:
            log.info("Resetting the device...")
            machine.reset()
