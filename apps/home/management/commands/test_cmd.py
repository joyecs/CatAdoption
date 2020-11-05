from django.core.management.base import BaseCommand, CommandError
#stdout something.
def _p(obj, msg, style_str='SUCCESS'):
    style = eval("obj.style.{}".format(style_str.upper()))
    return obj.stdout.write(style(msg))
#===end of _p
class Command(BaseCommand):
    help = "this is command test's help text"

    def add_arguments(self, parser):
        #nargs: + means at least 1, ? mean one or no, * means 0-n; 1 means only 1
        #type: floatt, int, str;
        parser.add_argument('arg1', nargs=1, type=int, help="arg1:int")
        parser.add_argument('arg2', nargs=1, type=str, help="arg2:string")
        parser.add_argument(
            '-t',
            '--test',
            type=str,
            help="optional arg",
            nargs="+",
        )
        parser.add_argument(
            '-f','--flag',
            help="this is flag option",
            action="store_true",
        )
    # def print(self, msg):
    #     self.stdout.write(msg)

    def handle(self, *args, **kwargs):
        self.stdout.write('handling test command')
        arg1 = kwargs['arg1']#list
        arg2 = kwargs['arg2']#list
        t = kwargs.get('test','')#value
        f = kwargs.get('flag','')#value

        #results:
        #test: test 1 2 -t a b -f
        print(arg1)#[1]
        print(arg2)#['2']
        print(t)#['a''b','c']
        print(f)#true
