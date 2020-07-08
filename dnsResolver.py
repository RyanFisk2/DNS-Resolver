
import dns.resolver

with open("domains.txt", "r") as inp:
	domains = inp.read().splitlines()

	for domain in domains:
		result = dns.resolver.query(domain, 'A')
		for ip in result:
			address = ip.to_text()
			print('IP', address)

			with open("ips.txt", "a") as out:
				out.write(domain + " ")
				out.write(address + "\n")

