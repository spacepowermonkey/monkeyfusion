import .config as conf



if __name__=="__main__":
    # Load the configuration as defined by parameters.
    parser = argparse.ArgumentParser(description='Stocks Package CLI')
    parser.add_argument("--confdir", dest="confdir", help="config directory")
    parser.add_argument("--config", dest="confname", help="config filename")
    args = parser.parse_args()

    config = conf.Config(args.confdir, args.confname)

    # For each spec in the config, load its data and generate images.
    for dataset in config.datasets:
        spider.connectors.sources[dataset.source].crawl(
            dataset.symbol, dataset.period, dataset.resolution
        )
        time.sleep(1)