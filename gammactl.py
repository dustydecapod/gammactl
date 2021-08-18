import click

from pydbus import SessionBus

# dbus setup
bus = SessionBus()
svc_proxy = bus.get('net.zoidplex.wlr_gamma_service',
        '/net/zoidplex/wlr_gamma_service')
brightnessctl = svc_proxy['net.zoidplex.wlr_gamma_service.brightness']
temperaturectl = svc_proxy['net.zoidplex.wlr_gamma_service.temperature']

_terse = False
_quiet = False

@click.group()
@click.option('--quiet', default=False, is_flag=True)
@click.option('--terse', default=False, is_flag=True)
def cli(quiet, terse):
    global _terse, _quiet
    _terse = terse
    _quiet = quiet

@cli.group()
def brightness():
    pass

@brightness.command()
def get():
    rval = round(brightnessctl.get(), 2)
    if _quiet: return
    if _terse: print(rval)
    print("Current brightness: %.2f (%i%%)" % (rval, rval*100))

@brightness.command()
@click.argument('value', default=1.0)
def set(value):
    rval = brightnessctl.set(value)
    if _quiet: return
    if _terse: print(rval)
    print("Current brightness: %.2f (%i%%)" % (rval, rval*100))

@brightness.command()
@click.argument('amount', default=0.05)
def increase(amount):
    rval = brightnessctl.increase(amount)
    if _quiet: return
    if _terse: print(rval)
    print("Current brightness: %.2f (%i%%)" % (rval, rval*100))

@brightness.command()
@click.argument('amount', default=0.05)
def decrease(amount):
    rval = brightnessctl.decrease(amount)
    if _quiet: return
    if _terse: print(rval)
    print("Current brightness: %.2f (%i%%)" % (rval, rval*100))

@cli.group()
def temperature():
    pass

@temperature.command()
def get():
    rval = temperaturectl.get()
    if _quiet: return
    if _terse: print(rval)
    print("Current temperature: %iK" % rval)

@temperature.command()
@click.argument('value', default=6500)
def set(value):
    rval = temperaturectl.set(value)
    if _quiet: return
    if _terse: print(rval)
    print("Current temperature: %iK" % rval)

@temperature.command()
@click.argument('amount', default=100)
def increase(amount):
    rval = temperaturectl.increase(amount)
    if _quiet: return
    if _terse: print(rval)
    print("Current temperature: %iK" % rval)

@temperature.command()
@click.argument('amount', default=100)
def decrease(amount):
    rval = temperaturectl.decrease(amount)
    if _quiet: return
    if _terse: print(rval)
    print("Current temperature: %iK" % rval)

