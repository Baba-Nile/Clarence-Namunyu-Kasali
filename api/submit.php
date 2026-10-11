<?php
// Form endpoint for shared hosting/cPanel. Sends each valid submission to the campaign inbox with mail().
// It stores nothing. It answers {"ok":true} ONLY when mail() accepted the message.
// GET ?status=1 returns {"configured":true|false} so the page can warn visitors honestly.
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
header('X-Content-Type-Options: nosniff');

function out($code, $arr) { http_response_code($code); echo json_encode($arr); exit; }
function clean($v, $max) { $v = is_string($v) ? trim($v) : ''; $v = preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F]/', '', $v); return function_exists('mb_substr') ? mb_substr($v, 0, $max) : substr($v, 0, $max); }
function oneline($v) { return trim(preg_replace('/[\r\n]+/', ' ', $v)); }

$cfgFile = __DIR__ . '/config.php';
$cfg = is_file($cfgFile) ? include $cfgFile : [];
$to = is_array($cfg) && isset($cfg['recipient']) ? trim($cfg['recipient']) : '';
$from = is_array($cfg) && isset($cfg['from']) ? trim($cfg['from']) : '';
$configured = function_exists('mail') && filter_var($to, FILTER_VALIDATE_EMAIL) && filter_var($from, FILTER_VALIDATE_EMAIL);

if ($_SERVER['REQUEST_METHOD'] === 'GET') out(200, ['configured' => (bool)$configured]);
if ($_SERVER['REQUEST_METHOD'] !== 'POST') out(405, ['ok' => false, 'error' => 'method']);
if (!$configured) out(503, ['ok' => false, 'error' => 'not_configured']);

if (clean($_POST['website'] ?? '', 200) !== '') out(200, ['ok' => true]); // honeypot: silently drop bots
$elapsed = (int)($_POST['elapsed'] ?? 0);
if ($elapsed < 3000) out(400, ['ok' => false, 'error' => 'too_fast']);

// Simple per-IP limit: 5 messages per hour, kept in the temp folder (no personal content stored).
$ip = $_SERVER['REMOTE_ADDR'] ?? 'x'; $rf = sys_get_temp_dir() . '/kasali_rl_' . sha1($ip);
$hits = is_file($rf) ? array_filter(array_map('intval', explode(',', (string)file_get_contents($rf))), function ($t) { return $t > time() - 3600; }) : [];
if (count($hits) >= 5) out(429, ['ok' => false, 'error' => 'rate']);

$type = clean($_POST['type'] ?? '', 20);
if (!in_array($type, ['community', 'volunteer', 'contact'], true)) out(400, ['ok' => false, 'error' => 'type']);
$wards = ['idakho-central' => 'Idakho Central', 'idakho-east' => 'Idakho East', 'idakho-north' => 'Idakho North', 'idakho-south' => 'Idakho South', 'other' => 'Other / not sure'];
$cats = ['gold' => 'Gold mining and miner safety', 'land' => 'Land rights and compensation', 'roads' => 'Roads and transport', 'water' => 'Water and environment', 'education' => 'Education', 'health' => 'Healthcare', 'agriculture' => 'Agriculture and livelihoods', 'youth' => 'Youth opportunities', 'other' => 'Other'];

$name = clean($_POST['name'] ?? '', 80); $phone = clean($_POST['phone'] ?? '', 30); $email = clean($_POST['email'] ?? '', 120);
$message = clean($_POST['message'] ?? '', 1500); $ward = clean($_POST['ward'] ?? '', 30); $cat = clean($_POST['category'] ?? '', 30);
$subject = clean($_POST['subject'] ?? '', 30); $areas = isset($_POST['areas']) && is_array($_POST['areas']) ? array_map(function ($a) { return clean($a, 60); }, array_slice($_POST['areas'], 0, 10)) : [];

if (clean($_POST['consent'] ?? '', 5) !== 'yes') out(422, ['ok' => false, 'error' => 'consent']);
if ($email !== '' && !filter_var($email, FILTER_VALIDATE_EMAIL)) out(422, ['ok' => false, 'error' => 'email']);
if ($ward !== '' && !isset($wards[$ward])) out(422, ['ok' => false, 'error' => 'ward']);
if ($cat !== '' && !isset($cats[$cat])) out(422, ['ok' => false, 'error' => 'category']);
if ($type === 'community' && ($ward === '' || $cat === '' || strlen($message) < 10)) out(422, ['ok' => false, 'error' => 'fields']);
if ($type === 'volunteer' && ($name === '' || $phone === '' || $ward === '' || !$areas)) out(422, ['ok' => false, 'error' => 'fields']);
if ($type === 'contact' && ($name === '' || $email === '' || strlen($message) < 10)) out(422, ['ok' => false, 'error' => 'fields']);

$lines = ["Form: $type", 'Ward: ' . ($wards[$ward] ?? '-'), 'Topic: ' . ($cats[$cat] ?? ($subject ?: '-')), 'Name: ' . ($name ?: '-'), 'Phone: ' . ($phone ?: '-'), 'Email: ' . ($email ?: '-')];
if ($areas) $lines[] = 'Volunteer areas: ' . implode(', ', $areas);
$lines[] = ''; $lines[] = $message;
$subj = '[Website] ' . ucfirst($type) . ($ward ? ' - ' . $wards[$ward] : '');
$headers = ['From: ' . $from, 'Content-Type: text/plain; charset=UTF-8', 'MIME-Version: 1.0'];
if ($email !== '') $headers[] = 'Reply-To: ' . oneline($email);
$subjEnc = function_exists('mb_encode_mimeheader') ? mb_encode_mimeheader($subj, 'UTF-8') : $subj;

if (!mail($to, $subjEnc, implode("\n", $lines), implode("\r\n", $headers))) out(502, ['ok' => false, 'error' => 'send_failed']);
$hits[] = time(); @file_put_contents($rf, implode(',', $hits));
out(200, ['ok' => true]);
